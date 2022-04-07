from __future__ import annotations


class ChristmasTreeFarm:
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int) -> None:
        self.plots: list[int] = []
        for i in range(0, initial_planting):
            self.plots.append(1)
        for j in range(plots - initial_planting):
            self.plots.append(0)

    def plant(self, index: int) -> None:
        self.plots[index] = 1

    def growth(self) -> None:
        i: int = 0 
        for tree in self.plots:
            if tree != 0:
                self.plots[i] += 1
                i += 1

    def harvest(self, replant: bool):
        i: int = 0 
        total: int = 0
        for tree in self.plots:
            if tree >= 5:
                total += 1
                if replant:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
            i += 1
    
    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        new_size = len(self.plots) + len(rhs.plots)
        total_trees: int = 0
        for tree in self.plots:
            if tree == 1:
                total_trees += 1
        
        for tree in rhs.plots:
            if tree == 1:
                total_trees += 1
            
        new_farm: ChristmasTreeFarm = ChristmasTreeFarm(new_size, total_trees)
        return new_farm


farm1: ChristmasTreeFarm = ChristmasTreeFarm(10, 5)
farm1.growth()
print(farm1.plots)


class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        if self.level > 400 and prereq in self.prerequisites:
            return True
        else:
            return False


def find_courses(classes: list[Course], prereq: str):
    names: list[str] = []
    for course in classes:
        if course.level > 400 and prereq in course.prerequisites:
            names.append(course.name)


class Pond: 
    ducks: list[str]
    bread_remaining: int

    def __init__(self, duck_list: list[str], bread: int):
        self.ducks = duck_list
        self.bread_remaining = bread

    def feed_duck(self):
        for duck in self.ducks:
            if self.bread_remaining < 2:
                print(f"{duck} didn't get fed.")
            else:
                self.bread_remaining -= 2
    
    def add_slices(self, num_slices: int):
        self.bread_remaining += num_slices