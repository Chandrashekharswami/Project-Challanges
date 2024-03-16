def get_value_from_nested_object(obj, key):
    keys = key.split('/')
    current = obj
    try:
        for k in keys:
            current = current[k]
        return current
    except KeyError:
        return None

#################
object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
print(get_value_from_nested_object(object1, key1))  

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
print(get_value_from_nested_object(object2, key2)) 
