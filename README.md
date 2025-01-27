# Mock Code Challenge - National Parks (Object Relationships)

For this assignment, we'll be working with a national park planner-style domain.

We have three models: `NationalPark`, `Visitor`, and `Trip`.

For our purposes, a `NationalPark` has many `Trip`s, a `Visitor` has many
`Trip`s, and a `Trip` belongs to a `Visitor` and to a `NationalPark`.

`NationalPark` - `Visitor` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

_Carefully consider where to create your Single Source of Truth._

### Initializers and Properties

#### Visitor

- `Visitor __init__(self, name)`
X- Visitor should be initialized with a name
- `Visitor property name`
X- Should return the visitor's name
X- Names must be of type `str`
X- Names must be between 1 and 15 characters, inclusive
X- `raise Exception` if setter fails

#### NationalPark

- `NationalPark __init__(self, name)`
X- national_parks should be initialized with a name, as a string
- `NationalPark property name`
X- Returns a given national_park's name
X- Should not be able to change after the national_park is created
X- `raise Exception` if setter fails
X- _hint: hasattr()_

#### Trip

- `Trip __init__(self, visitor, national_park, start_date, end_date)`
X- Trips should be initialized with a visitor, national_park, start_date(str), end_date(str)

### Object Relationship Methods and Properties

#### Trip

- `Trip property visitor`
 X- Returns the visitor object for that trip
 X- Must be of type `Visitor`
 X- `raise Exception` if setter fails
- `Trip property national_park`
 X- Returns the NationalPark object for that trip
 X- Must be of type `NationalPark`
 X- `raise Exception` if setter fails

#### Visitors

- `Visitor trips(self)`
 X- Returns a list of all trips for that visitor
 X- The list of trips must contain type `Trip`
 _______________________________
- `Visitor national_parks(self)`
  - Returns a **unique** list of all parks which that visitor has visited.
  - The list of national parks must contain type `NationalPark` 

#### NationalPark

- `NationalPark trips(self)`
 X- Returns a list of all trips planned for this national park
 X- The list of trips must contain type `trip`
 ______________________________
- `NationalPark visitors(self)`
  - Returns a **unique** list of all visitors a national park has recieved
  - The list of visitors must contain type `Visitor`

### Aggregate and Association Methods

#### National Park

- `NationalPark total_visits(self)`
 X - Returns the total number of times that park has been visited
 __________________________________
 ### BONUS
- `NationalPark best_visitor(self)`
 - Returns the Visitor who has visited the park the most
- `NationalPark classmethod most_visited(cls)`
  - Returns the national_park which has received the most visits