from scipy.stats import norm
import random
import math
import numpy as np

# generates firms' resume scores for each applicant, returns a dictionary
# an applicant's resume score is picked from a probability distribution, so firms give similar but not identical ratings 
def generate_resume_scores(firms, applicants):
    F = len(firms)
    N = len(applicants)
    # what we will return: a dictionary representing each firms resume score of all the applicants
    firms_score_applicants = {}
    # the mean score for each applicant, used to create a normal distribution 
    mean_scores = np.zeros(N, dtype=int)

    # for each applicant
    for a in range(0, N):
        # mean score is generated randomly
        mean_scores[a] = random.randint(1, 100)

    for f in range(0, F):
        # go through all the firms
        firm_name = firms[f]
        # all the applicants' real resume scores, sampled from their respective normal distributions
        actual_scores = []
        # for each applicant, sample a resume score based on their previosly decided mean score
        for a in range(0, N):
            sample = norm.rvs(loc=mean_scores[a], size=1)[0] # first element of resulting array, so 'sample' is an integer
            app_res_score = {'name': applicants[a], 'score': sample}
            # actual_scores is a list of dictionaries where applicants are matched with their resume scores
            actual_scores.append(app_res_score)

        firms_score_applicants[firm_name] = actual_scores

    return firms_score_applicants

# after firms have scored each applicant's resume, they keep the top 20% of applicants to interview
# 'keep' is a percentage representing how many applicants to retain after resume screening round
# returns a dictionary where firms are matched with a truncated, ordered list of applicants and their scores
def resume_screening(firms, applicants, firms_score_applicants, keep):
    F = len(firms) 
    N = len(applicants) 
    firms_score_applicants_top = {} # firms' applicant scores after they have truncated their list based on resume scores

    k = math.floor(keep * N) # the number of applicants we will interview after resume round
    print('k',k)
    for f in range(0, F):
        firm_name = firms[f]
        sorted_res_scores = sorted(firms_score_applicants[firm_name], key=lambda x: x['score'], reverse=True)
        firms_score_applicants_top[firm_name] = sorted_res_scores[:k] # truncate to only keep top k candidates
        
    return firms_score_applicants_top

# converting our dictionaries to a format that is compatible with DA code (previous two functions return dictionary of dictionaries)
def convert_to_preferences(firms, new_app_list, firms_score_applicants_top):
    F = len(firms)
    N = len(new_app_list)

    # what we will return: a dictionary of firms to their list of applicant preferences where applicants are identified by place in applicant list
    firms_preferences = {}
    # for each firm
    for f in range(0, F):
        firm_name = firms[f]
        # a list of dictionaries where each item is {'name': name, 'score', score}
        applicant_scores = firms_score_applicants_top[firm_name] 
        # a list of dictionaries but sorted numerically by score highest to lowest
        sorted_applicant_scores = sorted(applicant_scores, key=lambda x: x['score'], reverse=True)
        preference = [] # the firm's preferences as a list where applicants are numbers based on their place in resume screened list
        for a in range(0, N):
            applicant_name = sorted_applicant_scores[a]['name']
            index = new_app_list.index(applicant_name) + 1 # applicant's place in resume screened list
            preference.append(index)
        firms_preferences[firm_name] = preference 

    return firms_preferences

# converts a list of format [{'name': name, 'score', score}, {'name': name, 'score', score}, ...] to a list of applicants
# used to build new applicant_list for each firm after initial resume screening
def dict_to_list(firms_score_resume_top):
    N = len(firms_score_resume_top) # number of remaining applicants after resume screening
    new_app_list = []
    for a in range(0, N):
        applicant_name = firms_score_resume_top[a]['name']
        new_app_list.append(applicant_name)
    return new_app_list
