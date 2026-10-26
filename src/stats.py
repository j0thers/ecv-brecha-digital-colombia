"""
Módulo de estadística inferencial y modelado econométrico.
"""
import pandas as pd
import numpy as np
from scipy import stats as scipy_stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

def chi2_independence_test(df: pd.DataFrame, var1: str, var2: str) -> dict:
    ct = pd.crosstab(df[var1], df[var2])
    chi2, p, dof, exp = scipy_stats.chi2_contingency(ct)
    n = ct.sum().sum()
    k = min(ct.shape) - 1
    cramer_v = np.sqrt(chi2 / (n * k)) if (n * k) > 0 else 0.0
    return {"chi2": float(chi2), "p_value": float(p), "dof": int(dof), "cramer_v": float(cramer_v), "n": int(n)}

def ci_proportions_difference(count1: int, n1: int, count2: int, n2: int, alpha: float = 0.05) -> dict:
    p1 = count1 / n1
    p2 = count2 / n2
    diff = p1 - p2
    se = np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    z = scipy_stats.norm.ppf(1 - alpha / 2)
    return {"diff": float(diff), "se": float(se), "ci_lower": float(diff - z * se), "ci_upper": float(diff + z * se)}

def fit_logistic_model(formula: str, data: pd.DataFrame) -> dict:
    model = smf.logit(formula, data=data).fit(disp=False)
    params = model.params
    conf = model.conf_int()
    conf.columns = ["ci_lower", "ci_upper"]
    or_df = pd.DataFrame({
        "OR": np.exp(params),
        "ci_lower": np.exp(conf["ci_lower"]),
        "ci_upper": np.exp(conf["ci_upper"]),
        "p_value": model.pvalues,
        "coef": params,
        "se": model.bse,
    })
    return {"model": model, "or_table": or_df, "prsquared": float(model.prsquared), "nobs": int(model.nobs)}
