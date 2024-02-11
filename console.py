#!/usr/bin/python3
"""Console module."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    
    """

    prompt = '(hbnb) '
    cls_dicteinary = {"BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review}

    def do_EOF(self, cmd_ln):
        """EOF command to exit the program."""
        return True

    def do_quit(self, cmd_ln):
        """Quit command to exit the program."""
        return True
    
    def help_quit(self, cmd_ln):
        """
        
        """
        print("Quit command to exit the program.")

    def emptyline(self):
        """Empty line."""
        pass

    def do_create(self, cmd_ln):
        """
        
        """
        if cmd_ln == "":
            print("** class name missing **")
            return
        else:
            try:
                var_cls = eval(cmd_ln + "()")
                var_cls.save()
                print(var_cls.id)
            except Exception as e:
                print("** class doesn't exist **")
                return

    def do_show(self, cmd_ln):
        """
        
        """
        cmd_vtr = cmd_ln.split()
        if cmd_vtr == []:
            print("** class name missing **")
            return
        elif self.cls_dicteinary.get(cmd_vtr[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(cmd_vtr) != 2:
            print("** instance id missing **")
            return
        cls_objs = storage.all()
        ky = cmd_vtr[0] + "." + cmd_vtr[1]
        if ky in cls_objs.keys():
            print(cls_objs[ky].__str__())
        else:
            print("** no instance found **")
            return

    def do_destroy(self, cmd_ln):
        """
        
        """
        cmd_vtr = cmd_ln.split()
        if cmd_vtr == []:
            print("** class name missing **")
            return
        elif self.cls_dicteinary.get(cmd_vtr[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(cmd_vtr) != 2:
            print("** instance id missing **")
            return

        cls_objs = storage.all()
        ky = cmd_vtr[0] + "." + cmd_vtr[1]
        if ky in cls_objs.keys():
            cls_objs.pop(ky)
            storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, cmd_ln):
        """
        
        """
        cmd_vtr = cmd_ln.split()

        objs_str_rprsntton = []
        cls2rprsnt = None
        if cmd_vtr != []:
            cls2rprsnt = cmd_vtr[0]
            if cls2rprsnt not in self.cls_dicteinary:
                print("** class doesn't exist **")
                return

        cls_objs = storage.all()
        for obj in cls_objs.values():
            if cls2rprsnt is None:
                objs_str_rprsntton.append(obj.__str__())
            elif obj.__class__.__name__ == cls2rprsnt:
                objs_str_rprsntton.append(obj.__str__())

        print(objs_str_rprsntton)

    def do_update(self, cmd_ln):
        """
        
        """
        cmd_vtr = cmd_ln.split()
        vctr_ln = len(cmd_vtr)
        if cmd_vtr == []:
            print("** class name missing **")
            return
        elif cmd_vtr[0] not in self.cls_dicteinary:
            print("** class doesn't exist **")
            return
        elif vctr_ln < 2:
            print("** instance id missing **")
            return
        else:
            cls_objs = storage.all()
            ky = cmd_vtr[0] + "." + cmd_vtr[1]

            if ky not in cls_objs.keys():
                print("** no instance found **")
                return
            elif vctr_ln < 3:
                print("** attribute name missing **")
                return
            elif vctr_ln < 4:
                print("** value missing **")
                return
            else:
                setattr(cls_objs[ky],
                        cmd_vtr[2],
                        eval(cmd_vtr[3]))
                cls_objs[ky].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

