"""file to define validations"""

class Validation:
    """
        Validations
    """
    EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    PHONE_REGEX = r"^[ ()\+\-\d]*$"
    password_pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+~\-=`{}\[\]:\";'<>?,.\/])(?=.*[a-zA-Z0-9]).{8,}$"

