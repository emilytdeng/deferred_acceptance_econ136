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
    mean_scores = np.zeros(N)

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
            print(a)
            sample = norm.rvs(loc=mean_scores[a], size=1)
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

    k = math.floor(keep * F) # the number of applicants we will interview after resume round
    for f in range(0, F):
        sorted_res_scores = sorted(firms_score_applicants[f], key=lambda x: x['score'], reverse=True)
        firms_score_applicants_top[f] = sorted_res_scores[:keep] # truncate to only keep top k candidates
        
    return firms_score_applicants_top

# converting our dictionaries to a format that is compatible with DA code (previous two functions return dictionary of dictionaries)
def convert_to_preferences(firms, applicants, firms_score):
    F = len(firms)
    N = len(applicants)

    # what we will return: a dictionary of firms to their list of applicant preferences where applicants are identified by place in original list
    firms_preferences = {}
    # for each firm
    for f in range(0, F):
        applicant_scores = firms_score[f] # a list of dictionaries where each item is {'name': name, 'score', score}
        sorted_applicant_scores = sorted(applicant_scores, key=lambda x: x['score'], reverse=True)
        preference = np.zeros(N) # the firm's preferences as a list where applicants are numbers based on their place in OG applicants list
        for a in range(0, N):
            index = applicants.index(sorted_applicant_scores['name']) + 1 # applicant's original place in 'applicants' list
            preference[a] = index
        firms_preferences[f] = preference 

    return firms_preferences
