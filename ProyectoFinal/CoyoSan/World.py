from CryptoPower import VerticalMP, HorizontalMP, CrossMP, ExtraLB, DoubleCrush
from CrytoBlock import UsdtBlock, BtcBlock, EthBlock, DogeBlock
from CoyoSan import CoyoSan
from LedgerBullet import LedgerBullet
from panda3d import *
from math import sqrt, cos, sin
from random import random

#Clase Padre
class DescentralWorld:
  HIGHT = 250
  WEIGHT = 120
  FLOORS = 20
  LINE = 6 
  def __init__(self,hight,weight,floors,lines):
    super().__init__(hight,weight,floors,lines)


# Colocando Crypto Blocks iniciales
  for i in range (0,20):
    self.UsdtBlock.append(
      UsdtBlocks(
        getRandomBetween(2,floors)
        getRandomBetween(0,lines)
        getRandomBetwen(MinCryptos, MaxCryptos)
      )
    )

  for i in range (0,2):
    self.BtcBlock.append(
      BtcBlocks(
        getRandomBetween(2,floors)
        getRandomBetween(0,lines)
        getRandomBetwen(MinCryptos, MaxCryptos)
      )
    )
  
  for i in range (0,8):
    self.EthBlock.append(
      EthBlocks(
        getRandomBetween(2,floors)
        getRandomBetween(0,lines)
        getRandomBetwen(MinCryptos, MaxCryptos)
      )
    )

  for i in range (0,26):
    self.DogeBlock.append(
      DogeBlocks(
        getRandomBetween(2,floors)
        getRandomBetween(0,lines)
        getRandomBetwen(MinCryptos, MaxCryptos)
      )
    )

#Colocando Crypto Powers iniciales
    for i in range (0,2):
      self.VerticalMP.append(
      VerticalMP(
        getRandomBetween(2,floors)
        getRandomBetween(0,lines)
      )
    )

    for i in range (0,2):
      self.HorizontalMP.append(
      HorizontalMP(
        getRandomBetween(2,floors)
        getRandomBetween(0,lines)
      )
    )

    for i in range (0,1):
      self.CrossMP.append(
      CrossMP(
        getRandomBetween(2,floors)
        getRandomBetween(0,lines)
      )
    )

    for i in range (0,5):
      self.ExtraLB.append(
      ExtraLB(
        getRandomBetween(2,floors)
        getRandomBetween(0,lines)
      )
    )

    for i in range (0,1):
        self.DoubleCrush.append(
      DoubleCrush(
        getRandomBetween(2,floors)
        getRandomBetween(0,lines)
      )
    )