from mysqlconnection import connectToMySQL

DATABASE = "users"

class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @classmethod
    def get_all(cels):
        query = """
            SELECT * FROM users;
        """

        results = connectToMySQL(DATABASE).query_db(query)

        users = []

        if results:
            for dict in results:
                new_user = User(dict)
                users.append(new_user)

        return users

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users(first_name, last_name, email) 
            VALUES(%(first_name)s, %(last_name)s, %(email)s)
        """

        return connectToMySQL(DATABASE).query_db(query, data)