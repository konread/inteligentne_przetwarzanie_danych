class FileManager(object):
    # N - the number of neuron's inputs
    def __init__(self):
        self.numberOfTrainingPatterns = 0
        # vertical resolution of the matrix of a single training standard (sign)
        self.verticalResolution = 0
        # horizontal resolution of the matrix of a single training standard (sign)
        self.horizontalResolution = 0

    def read(self, fileName):
        with open(fileName) as file:
            self.numberOfTrainingPatterns = int(file.readline())
            self.verticalResolution = int(file.readline())
            self.horizontalResolution = int(file.readline())
            self.signsWithMatrices = []

            for _ in range(self.numberOfTrainingPatterns):
                sign = str(file.readline().rstrip('\n'))
                pattern = []
                for _ in range(self.verticalResolution):
                    line = str(file.readline().rstrip('\n'))
                    pattern.extend(self.decode(line))
                self.signsWithMatrices.append(tuple([sign, pattern]))

        return self

    def decode(self, line):
        pattern = []
        for item in line:
            if item == '#':
                pattern.append(1)
            else:
                pattern.append(0)


        return pattern