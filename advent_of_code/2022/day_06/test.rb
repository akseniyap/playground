require "minitest/autorun"
require_relative "solution"


class Day06 < MiniTest::Test
  def test_easy_1
    data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    result = easy(data)
    assert_equal 7, result
  end

  def test_easy_2
    data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    result = easy(data)
    assert_equal 5, result
  end

  def test_easy_3
    data = "nppdvjthqldpwncqszvftbrmjlhg"
    result = easy(data)
    assert_equal 6, result
  end

  def test_easy_4
    data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    result = easy(data)
    assert_equal 10, result
  end

  def test_easy_5
    data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    result = easy(data)
    assert_equal 11, result
  end

  def test_hard_1
    data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    result = hard(data)
    assert_equal 19, result
  end

  def test_hard_2
    data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    result = hard(data)
    assert_equal 23, result
  end

  def test_hard_3
    data = "nppdvjthqldpwncqszvftbrmjlhg"
    result = hard(data)
    assert_equal 23, result
  end

  def test_hard_4
    data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    result = hard(data)
    assert_equal 29, result
  end

  def test_hard_5
    data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    result = hard(data)
    assert_equal 26, result
  end
end
