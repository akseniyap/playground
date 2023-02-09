require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.open("inputs/05_#{variation}.txt").read
end

def modify(data)
  data = data.split(NEW_LINE)
  separator = data.find_index("")
  levels, instructions = data[..separator-2], data[separator+1..]
  levels = levels.map { |line| line.gsub("    ", " [-] ") }
                 .map { |line| line.scan(/[A-Z-]/) }

  return levels, instructions
end

def get_data(variation)
  levels, instructions = modify(raw_data(variation))
  stacks = build_start_state(levels)
  instructions = parse_instructions(instructions)

  return stacks, instructions
end

def build_start_state(levels)
  stacks = Array.new(levels[-1].size+1){ [] }
  levels.reverse.each do |level|
    level.each.with_index(1) do |crate, index|
      unless crate == "-"
        stacks[index].append(crate)
      end
    end
  end

  stacks
end

def parse_instructions(instructions)
  instructions.map do |instruction|
    instruction.match(/move (\d+) from (\d+) to (\d+)/)
               .captures
               .map(&:to_i)
  end
end

def easy(data)
  stacks, instructions = *data

  instructions.each do |qty, from, to|
    qty.times do
      crate = stacks[from].pop
      stacks[to].push(crate)
    end
  end

  stacks.map { |stack| stack[-1] }.join
end

def hard(data)
  stacks, instructions = *data

  instructions.each do |qty, from, to|
    crates_to_move = stacks[from].pop(qty)
    stacks[to].push(*crates_to_move)
  end

  stacks.map { |stack| stack[-1] }.join
end

if __FILE__ == $0
  data = get_data(INPUT)
  puts easy(data)
  puts hard(data)
end
