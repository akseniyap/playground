from dataclasses import dataclass


@dataclass
class Elf:
    start: int
    end: int

    def contains(self, other):
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other):
        return self.start <= other.start <= self.end
