from random import randrange

class SivirMessages:
  fun = [
    ". I still think that's better nerf Irelia.",
    ", because MORDEKAISER ES NUMERO UNO!",
    ". OR FEED.",
    ". BRONZODIA!",
    ". Looks like your trying to make an AD Lux!",
    ". OR I REPORT U."
  ]

  def __init__(self): pass

  @classmethod
  def get_rand_message(self):
    return self.fun[randrange(len(self.fun))]

  @classmethod
  def make_answer(self, required_options):
    message = "[Sivir] Please, fill: "
    if (type(required_options) is list):
      message += " and ".join(required_options)
    else:
      message += required_options
    return message

  @classmethod
  def error(self, required_options):
    rand_fun = self.get_rand_message()
    message = self.make_answer(required_options) + rand_fun
    raise Exception(message)
