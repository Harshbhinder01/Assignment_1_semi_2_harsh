from email_validator import validate_email, EmailNotValidError


class Client:
    """
    this is the Client class 
    """

    def __init__(self, client_number : int, first_name : str, last_name : str, email_address: str):
        """
        args:
        client_number(int): An integer vaule that representing the client number
        first_name(str): A string value the clients first name.
        last_name(str): A string value the clients last name.
        email_address(str): A string value the clients email address.
        
        ValueError:
        client_number(int): if the value is not a int raise ValueError
        first_name(str): if the first name is blank raise a ValueError
        last_name(str): if the last name is blank raise a ValueError
        email_address(str): raise a ValueError if the email address is invalid
        """
        #if the value is not a int raise ValueError
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("The client number must be a integer.")

        #if the first name is blank raise a ValueError
        if len(first_name.strip()) == 0:
            self.__first_name = first_name
        else:
            raise ValueError("The first name cannot be blank")

        #if the last name is blank raise a ValueError
        if len(last_name.strip()) == 0:
            self.__last_name = last_name
        else:
            raise ValueError("The last name cannot be blank.")
        # if the email address is invalid raise a EmailNotValidError
        try:
            valid_email = validate_email(email_address)
            self.__email_address = valid_email.email
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"    

    @property
    def client_number(self) -> int:
        """ 
        this returns the client number
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """ 
        this returns the first name
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """ 
        this returns the last name
        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """ 
        this returns the email address
        """
        return self.__email_address

    def __str__(self) ->str :
        """this shows a string of the client"""
        return f"{self.last_name},{self.first_name}, [{self.client_number}], {self.email_address}]"
    
    
            
            

        
        