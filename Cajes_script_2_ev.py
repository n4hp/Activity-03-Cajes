class pokeev():
    def statD(base,iv,ev,Level):
        return(((2*base)+iv+(ev/4))*(Level/100))
  
    def statEvs(stats,nature,d,Level):
        return(((((stats/nature)-d)*400)/Level)/4)*4 