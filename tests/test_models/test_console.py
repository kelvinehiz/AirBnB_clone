#!/usr/bin/python3
"""Test code for AirBnB console."""

import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse_arguments(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class TestAirBnBConsole(cmd.Cmd):
    """Test command interpreter for AirBnB project."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel", "User", "State", "City",
        "Place", "Amenity", "Review"
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def default(self, arg):
        """Handle default command behavior."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exit the test console."""
        return True

    def do_EOF(self, arg):
        """Exit the test console at EOF."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance."""
        argl = parse_arguments(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in TestAirBnBConsole.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(argl[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show string representation of an instance."""
        argl = parse_arguments(arg)
        obj_dict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in TestAirBnBConsole.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Destroy an instance."""
        argl = parse_arguments(arg)
        obj_dict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in TestAirBnBConsole.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Display string representations of all instances."""
        argl = parse_arguments(arg)
        if len(argl) > 0 and argl[0] not in TestAirBnBConsole.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(argl) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """Count the number of instances."""
        argl = parse_arguments(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update an instance."""
        argl = parse_arguments(arg)
        obj_dict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in TestAirBnBConsole.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    TestAirBnBConsole().cmdloop()

