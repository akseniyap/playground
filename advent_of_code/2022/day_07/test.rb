require "minitest/autorun"
require_relative "solution"
require_relative "../utils/ruby_utils/constants"


class Day07 < MiniTest::Test
  def setup
    @data = raw_data(SAMPLE)
  end

  def test_easy
    result = easy(@data)
    assert_equal 95_437, result
  end

  def test_hard
    result = hard(@data)
    assert_equal 24_933_642, result
  end
end
