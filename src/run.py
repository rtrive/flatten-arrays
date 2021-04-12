import logging

logging.basicConfig(level=logging.INFO)


def flatten_array(array: list) -> list:
    """
    Take array as input and check if there are arrays inside.
    Transform array of array into single array and return it

    Parameters
    ----------
    array: list

    """
    if len(array) == 0:
        return []
    tmp_array: list = []
    for element in array:
        if type(element) is not list:
            logging.debug(f"Element {element} is a list")
            tmp_array.append(element)
        else:
            tmp_array += flatten_array(element)
    return tmp_array


if __name__ == "__main__":
    logging.info(f"Case one [1,2,3] -> {flatten_array([1,2,3])}")
    logging.info(f"Case two [1,[2],3] -> {flatten_array([1,[2],3])}")
    logging.info(f"Case three [1,[2,3]] -> {flatten_array([1,2,3])}")
    logging.info(f"Case four [[1],[2],[3]] -> {flatten_array([1,2,3])}")
