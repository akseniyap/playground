require "minitest/autorun"
require_relative "solution"
require_relative "../utils/ruby_utils/constants"


class Day05 < MiniTest::Test
  def setup
    @data = get_data(SAMPLE)
  end

  def test_easy
    result = easy(@data)
    assert_equal "CMZ", result
  end

  def test_hard
    result = hard(@data)
    assert_equal "MCD", result
  end
end
