class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

    def patient_profile(self):
        patient_information = {}
        patient_information["Name"] = self.name
        patient_information["Age"] = self.age
        patient_information["Sex"] = self.sex
        patient_information["BMI"] = self.bmi
        patient_information["Number of Children"] = self.num_of_children
        patient_information["Smoker"] = self.smoker
        return patient_information

    def update_age(self, new_age):
        self.age = new_age

        print(f"{self.name} is now {self.age} years old.")

        self.estimated_insurance_cost()

    def update_num_children(self, new_num_children):
        self.num_of_children = new_num_children

        print(f"{self.name} has {self.num_of_children} children."
              if self.num_of_children > 1 else
              f"{self.name} has {self.num_of_children} child.")

        self.estimated_insurance_cost()

    def estimated_insurance_cost(self):
        estimated_insurance_cost = 250 * self.age \
                                 - 128 * self.sex \
                                 + 370 * self.bmi \
                                 + 425 * self.num_of_children \
                                 + 24000 * self.smoker \
                                 - 12500

        print(
            f"{self.name}'s estimated insurance costs is {estimated_insurance_cost:.2f} dollars."
        )


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.patient_profile())
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(2)
print(patient1.patient_profile())