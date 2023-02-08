class Elf < Struct.new(:start, :end)
    def contains?(other)
      self.start <= other.start and self.end >= other.end
    end

    def overlaps?(other)
      self.start.between?(other.start, other.end)
    end
  end
