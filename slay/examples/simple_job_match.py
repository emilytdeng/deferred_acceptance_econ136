from deferred_acceptance.deferred_acceptance import deferred_acceptance
from deferred_acceptance.utils import create_dataframes
from data_generation.applicants_rank_firms import applicants_rank_firms
from data_generation.firms_score_applicants import generate_resume_scores, resume_screening, convert_to_preferences


def simple_job_match() -> None:
    """
    Here is a minimalistic example of deferred acceptance algorithm for firm-applicant job matching.
    """
    # Prepare the dataframes
    applicants = ["emily", "shaurya", "melina", "ellie"]
    firms = ["McKinsey", "Bain", "BCG"]
    students_preferences = applicants_rank_firms(applicants, firms, 1)
    res_scores = generate_resume_scores(firms, applicants)
    print(res_scores)
    res_screen = resume_screening(firms, applicants, res_scores, .2)
    print(res_scores)
    schools_preferences = convert_to_preferences(firms, applicants, res_screen)
    print(schools_preferences)

    students_df, schools_df = create_dataframes(
        students_list=applicants,
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
