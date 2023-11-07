class calculator:
    @staticmethod
    def dotproduct(V1: 'list[float]', V2: 'list[float]') -> None:
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: 'list[float]', V2: 'list[float]') -> None:
        result = [float(V1[i]) + V2[i] for i in range(len(V1))]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: 'list[float]', V2: 'list[float]') -> None:
        result = [float(V1[i]) - V2[i] for i in range(len(V1))]
        print(f"Sous Vector is : {result}")
