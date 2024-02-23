"""
Estimate the return with Monte Carlo evaluations
"""
def estimate_return_MonteCarlo(policy):
    sum=0
    for _ in range(0,n):
        sum+ = world_simulation(policy)
    return J(policy)=sum/n

"""
(Almost unbiased) Estimate the policy gradient via finite differences (ground truth)
"""
def estimate_gradient_finite_difference(f , delta):
    mean_return=estimate_return_MonteCarlo(f)
    f_delta=[]
    for i in range(0,len(f.weight)):
        # give finite difference on weight[i] for policy
        f.weight[i]+=delta
        # difference between expectation with difference and the one without variance
        f_delta_i=estimate_return_MonteCarlo(f)-mean_return

        f_delta.append(f_delta_i/ delta)
        f.weight[i] -= delta
    return f_delta
"""
our algorithm to get the gradient estimates using the gradient critic equation (1)
• we compute bias (squared average distance between gradient estimates and ground truth)
Equation : \nabla_{\theta}J(\theta)\approx E_{\tau_\beta}[\sum_{t=0}^\infty\gamma^t\lambda^t(g_t+(1-\lambda)\Gamma^\pi(s_t,A_t^\pi))] 
"""
def estimate_gradient_critic(policy):
    sum=0
    for i in range(0,n):
        sample intial state s
        para=1/(gamma*lamda)
        while episode is not end:
            para*=(gamma*lamda)
            act = policy(s)
            Policy_Gradient, Gradient_Critic = TDRC_gamma(s,a)
            sum+=para*(Policy_Gradient+(1-lamda)*Gradient_Critic)
            s=model(s,a)
    return sum/n

def compute_bias(values,ground_truth):
    return np.mean(np.mean([value - ground_truth for value in values], axis=0)**2)


def compute_var(values):
    return np.mean(np.std(values, axis=0)**2)


def compute_mse(values, ground_truth):
    return np.mean([(value - ground_truth)**2 for value in values])

for (policy, critic, off_policy) in []
   ground_truth=stimate_gradient_finite_difference(policy , delta):
   gc=estimate_gradient_critic(policy)
   compute_bias(gc, ground_truth)
   compute_var(gc)
   compute_mse(gc, ground_truth)