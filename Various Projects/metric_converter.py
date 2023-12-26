# Write a program that takes as input a string (from the terminal) in the form of either “.<number>KM” (for kilometers)
# or “<number>MI” (for miles). For example: “120KM” or “120MI”. If it is KM, it should print its mile equivalent,
# if it is MI, it should print its kilometers equivalent. You can take 1 mile == 1.6 kilometers and you can round
# the floats to integer. For example: if input is “120KM” it should print “120KM = 75MI”. If input is “120MI” it
# should print “120MI = 193KM”.

# s[len(s)-2:len(s)]

def get_metric_and_value():
    while True:
        distance = input("Enter your distance: ")

        if len(distance) < 3:
            print("Please enter valid format.")
            continue

        metric = distance[len(distance)-2:len(distance)]
        try:
            value = int(distance[0:len(distance)-2])
        except ValueError as e:
            print("Please enter numeric value.")
            continue

        if metric.upper() != "KM" and metric.upper() != "MI":
            print("Invalid metric")
            continue

        return (metric, value)

############################################

def convert(metric, value):
    if metric.upper() == "KM":
         print("Result is: " + str(value / 1.6) + "MI")
    elif metric.upper() == "MI":
        print("Result is: " + str(value * 1.6) + "KM")

############################################

(metric, value) = get_metric_and_value()
convert(metric, value)