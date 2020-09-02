def match_section(line, section):
    """Returns true if line matches section"""
    if line.startswith('----') and '---- ' + section in line:
        return True
    return False


class ShowTech:
    """Parser for sections in a Cisco show tech"""

    def __init__(self, show_tech_file):
        with open(show_tech_file) as f:
            self.shtech = f.read().splitlines()

    def get_section(self, sec_heading='show', sec_name=None):
        """Returns a section matching --- sec_heading sec_name"""
        text = []
        save_line = False
        for line in self.shtech:
            # Stop at the next section heading (if found)
            if match_section(line, sec_heading):
                save_line = False
            # Save all the lines in this section so we can return them
            if save_line:
                # Don't include blank lines
                if line != '':
                    text.append(line)
            # If the target section has found start saving lines
            if match_section(line, sec_heading+' '+sec_name):
                save_line = True
        return text

    def get_show_section(self, sec_name):
        """Returns the first show section matching sec_name"""
        return self.get_section(sec_heading='show', sec_name=sec_name)
