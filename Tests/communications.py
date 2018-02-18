from ..Modules.Communications import communications

class test_command_handler:
    def test(self, parameters):
        output = "Look what i got : </br>" + str(parameters)
        return output

handler = test_command_handler()
communications_thread_test = communications.communications(handler)
communications_thread_test.start()

should_run = True

while should_run:
    try:
        pass
    except KeyboardInterrupt:
        should_run = False

communication_thread_test.stop()
