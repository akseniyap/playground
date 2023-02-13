require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.readlines("inputs/07_#{variation}.txt",  chomp: true)
end

$file_system = {ROOT => {}}
def build_file_tree(data)
  current_path = []

  data.each do |line|
    case line
      when /\$ cd \.\./
        current_path.pop

      when /\$ cd (.+)/
        current_path << $1

      when /dir (\w+)/
        $file_system.dig(*current_path)[$1] = {}

      when /(\d+) (.+)/
        $file_system.dig(*current_path)[$2] = $1.to_i
    end
  end
end

$dir_sizes = {}
def dir_sizes(file_system, path)
  size = 0

  file_system.each do |dir_name, content|
    if content.class == Hash
      path << dir_name
      size += dir_sizes(file_system[dir_name], path)
    else
      size += content
    end
  end

  $dir_sizes[path.join("/")] = size
  path.pop

  size
end

def easy(data)
  build_file_tree(data)
  dir_sizes($file_system[ROOT], [ROOT])

  size_limit = 100_000

  $dir_sizes.values.filter { |size| size <= size_limit }.sum
end

def hard(data)
  build_file_tree(data)
  dir_sizes($file_system[ROOT], [ROOT])

  total_space = 70_000_000
  needed_space = 30_000_000
  free_space = total_space - $dir_sizes[ROOT]
  need_to_free = needed_space - free_space

  $dir_sizes.values.filter { |size| size >= need_to_free }.min
end

if __FILE__ == $0
  data = raw_data(INPUT)
  puts easy(data)
  puts hard(data)
end
