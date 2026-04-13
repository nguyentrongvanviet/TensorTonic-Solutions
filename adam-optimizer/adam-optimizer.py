import numpy as np
def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    m=np.array(m) 
    v=np.array(v) 
    grad=np.array(grad)
    m_old = beta1*m+(1-beta1)*grad 
    v_old = beta2*v+(1-beta2)*(grad**2) 
    m_new = m_old/(1-(beta1**t))
    v_new = v_old/(1-(beta2**t)) 
    param = param-lr*m_new/(np.sqrt(v_new)+eps)
    return param,m_old,v_old
    # Write code here
    pass
    