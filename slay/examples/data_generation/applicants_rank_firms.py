import random
import numpy as np

# F = number of firms
# N = number of applicants
# r = weight of the first firm in an applicant's priority list, used to determine how similar the applicants' firm rankings will be

# generates applicant priority lists over firms using weights
# returns a dictionary
def applicants_rank_firms(applicants, firms, r):
    F = len(firms)
    N = len(applicants)

    # an array representing each applicants ranking of every firm where firms are identified by name
    app_rankings_of_firms = {}

    # compute weights using the rho
    if r == 1:
        # applicants will have dissimilar rankings of firms
        weights = np.ones(F)/F
    else: 
        weights = np.zeros(F)
        rx = (r - 1)/(r**S - 1)
        for i in range(0, F):
            weights[i] = rx*(r**i)

    # returns an array, xP, containing each applicant's rankings of the firms
    for i in range(0, N):
        app_name = applicants[i]
        print(app_name)
        app_rankings_of_firms[app_name] = np.random.choice(F, F, replace=False, p=weights)
        for j in range(0, F):
            app_rankings_of_firms[app_name][j] += 1

    # returns a dictionary in the format compatible with deferred_acceptance.py
    return app_rankings_of_firms