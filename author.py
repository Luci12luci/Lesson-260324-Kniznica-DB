class Autor:
    def __init__(self, autor_id, name, bio):
     self.autor_id = autor_id
     self.name = name
     self.bio = bio

     def __str__(self):
         return f"---Autor---\nID Autor: {self.id}\nMeno: {self.name}\nBio: {self.bio}"
