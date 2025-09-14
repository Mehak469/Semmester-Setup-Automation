"""
    Automate semmester Structure Creation
"""
from config import setup
import os

def create_semester_structure():

    semester=input("Enter Semester Name: ").strip()
    subjects=input("Enter subjects (comma seperated): ").split(",")

    base_path=os.path.join(setup.BASE_DIR,setup.safe_name(semester))
    os.makedirs(base_path,exist_ok=True)

    for subject in subjects:
        subject=setup.safe_name(subject)
        subject_path=os.path.join(base_path,subject)
        os.makedirs(subject_path,exist_ok=True)

        for sub in setup.SUBFOLDERS:
            os.makedirs(os.path.join(subject_path,sub),exist_ok=True)
    

    print(f"\n✅ Semester setup created at: {base_path}")


if __name__ == "__main__":
    create_semester_structure()