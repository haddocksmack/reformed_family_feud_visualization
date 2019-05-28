import csv

class Question():
    """A class to organize data from each question of Reformed Family Fued"""
    
    def __init__(self, filename):
        """Initializes class settings"""
        self.filename = filename
        self.svg_name = filename[5:-4] + '.svg'
        self.question_text = ""
        self.raw_list = []
        self.sorted_list = []
        self.count_dict = {}
        
        # Calls func that creates lists of data
        self.get_lists()
        
        # Generates a dict with {'Sorted answer': number of answers} format
        self.get_count_dict(self.sorted_list)
        
        self.labels = sorted(self.count_dict, key=self.count_dict.__getitem__)
        self.plot_dicts = []
        
        self.get_plot_dicts()
    
    def get_lists(self):
        """Gets a list of the values of results"""
        with open(self.filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header_text = next(reader)
            next(reader)
            next(reader)
            
            # Generate lists
            for row in reader:
                self.raw_list.append(row[0].strip())
                self.sorted_list.append(row[1].strip())
            
            # Get question text
            self.question_text = header_text[0]
            
    def get_count_dict(self, list):
        """Generates a dict with {'Sorted answer': number of answers} format"""
        self.count_dict = dict((i, list.count(i)) for i in list)
        
    def get_plot_dicts(self):
        """Generates a list of dicts that are used in rendering chart."""
        for value in sorted(self.count_dict.values()):
            plot_dict = {
                'value': value
                }
            self.plot_dicts.append(plot_dict)   