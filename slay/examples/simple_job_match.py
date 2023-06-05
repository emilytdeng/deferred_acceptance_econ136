from deferred_acceptance.deferred_acceptance import deferred_acceptance
from deferred_acceptance.utils import create_dataframes
from data_generation.applicants_rank_firms import applicants_rank_firms
from data_generation.firms_score_applicants import generate_resume_scores, resume_screening, convert_to_preferences, dict_to_list


def simple_job_match() -> None:
    """
    Here is a minimalistic example of deferred acceptance algorithm for firm-applicant job matching.
    """
    # Prepare the dataframes
    applicants = ["emily", "shaurya", "melina", "ellie", "maya", "kyle", "ethan", "jamie", "ari", "chelsea"]
    firms = ["McKinsey", "Bain", "BCG"]
    students_preferences = applicants_rank_firms(applicants, firms, 1)
    res_scores = generate_resume_scores(firms, applicants)
    #print(res_scores)
    # each firm conducts resume screening and only picks their top 40% of candidates to interview
    for firm in firms:
        res_screen = resume_screening(firms, applicants, res_scores, 1)
        #print('res_screen', res_screen)
        screened_applicants = dict_to_list(res_screen)
        print(screened_applicants)
        schools_preferences = convert_to_preferences(firms, screened_applicants, res_screen)
        #print(schools_preferences)

        students_df, schools_df = create_dataframes(
            students_list=screened_applicants,
            students_preferences=students_preferences,
            schools_list=firms,
            schools_preferences=schools_preferences,
        )

        # Run the algorithm
        schools_quota = {"McKinsey": 1, "Bain": 2, "BCG": 1}
        matches = deferred_acceptance(
            students_df=students_df, schools_df=schools_df, schools_quota=schools_quota
        )

    print(matches)


if __name__ == "__main__":
    simple_job_match()
