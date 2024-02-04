from main import canJump
import pytest


def test1():
  nums = [2, 3, 1, 1, 4]
  acutal = canJump(nums)
  assert acutal


def test2():
  nums = [3, 2, 1, 0, 4]
  acutal = canJump(nums)
  assert not acutal


def test3():
  nums = [1, 1, 1, 1]
  acutal = canJump(nums)
  assert acutal


def test4():
  nums = [0]
  acutal = canJump(nums)
  assert acutal