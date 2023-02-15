require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.readlines("inputs/07_#{variation}.txt",  chomp: true)
end

class ElfFile
  attr_accessor :name, :size

  def initialize(name, size, parent)
    @name = name
    @size = size
    @parent = parent
  end

  def inspect
    "ElfFile(name: '#{@name}', parent: #{@parent.name})"
  end
end

class ElfDirectory
  attr_accessor :name, :parent, :content

  def initialize(name, parent)
    @name = name
    @parent = parent
    @content = []
  end

  def inspect
    "ElfDirectory(name: '#{@name}', content: #{@content.size}, parent: #{@parent.name})"
  end

  def size
    @content.map { |item| item.size }.sum
  end

  def add_item(item)
    @content << item
  end

  def find_dir(name)
    @content.find { |item| item.name == name }
  end

  def flatten_directories
    @content.grep(ElfDirectory).reduce([]) do |acc, directory|
      acc << directory
      acc += directory.flatten_directories
    end
  end
end

class ElfFileSystem
  attr_accessor :tree

  def initialize
    @tree = ElfDirectory.new("/", nil)
  end

  def size
    @tree.size
  end

  def flatten_directories
    @tree.flatten_directories
  end

  class << self
    def build_tree(data)
      file_system = ElfFileSystem.new
      location = file_system.tree

      data.drop(1).each do |line|
        case line
          when /\$ cd \.\./
            location = location.parent

          when /\$ cd (.+)/
            location = location.find_dir($1)

          when /dir (\w+)/
            dir = ElfFileSystem.mkdir($1, location)
            location.add_item(dir)

          when /(\d+) (.+)/
            file = ElfFileSystem.mkfile($2, $1.to_i, location)
            location.add_item(file)
        end
      end

      file_system
    end

    def mkfile(name, size, parent)
      ElfFile.new(name, size, parent)
    end

    def mkdir(name, parent)
      ElfDirectory.new(name, parent)
    end
  end
end

def easy(data)
  file_system = ElfFileSystem.build_tree(data)
  directories = file_system.flatten_directories

  size_limit = 100_000
  directories.filter { |dir| dir.size <= size_limit }.map(&:size).sum
end

def hard(data)
  file_system = ElfFileSystem.build_tree(data)
  directories = file_system.flatten_directories

  total_space = 70_000_000
  needed_space = 30_000_000
  free_space = total_space - file_system.size
  need_to_free = needed_space - free_space
  directories.filter { |dir| dir.size >= need_to_free }.map(&:size).min
end

if __FILE__ == $0
  data = raw_data(INPUT)
  puts easy(data)
  puts hard(data)
end
