require_relative "../utils/ruby_utils/constants"


def raw_data(variation)
  File.readlines("inputs/02_#{variation}.txt",  chomp: true)
end

def modify(data)
  data.map { |line| line.split }
end

MOVE_SCORE = {"X" => 1, "Y" => 2, "Z" => 3}
OUTCOME = {
    "AX" => 3, "AY" => 6, "AZ" => 0,
    "BX" => 0, "BY" => 3, "BZ" => 6,
    "CX" => 6, "CY" => 0, "CZ" => 3
}
OPTION_FOR_OUTCOME = {
    "AX" => "Z", "AY" => "X", "AZ" => "Y",
    "BX" => "X", "BY" => "Y", "BZ" => "Z",
    "CX" => "Y", "CY" => "Z", "CZ" => "X"
}

def easy(data)
  score = 0
  moves = modify(data)

  moves.each do |his, my|
    score += OUTCOME[his + my]
    score += MOVE_SCORE[my]
  end

  score
end

def hard(data)
  score = 0
  moves = modify(data)

  moves.each do |his, needed_outcome|
    my = OPTION_FOR_OUTCOME[his + needed_outcome]
    score += OUTCOME[his + my]
    score += MOVE_SCORE[my]
  end

  score
end

if __FILE__ == $0
  data = raw_data(INPUT)
  puts easy(data)
  puts hard(data)
end
