from script import Pokemon, FunctionsTestManual

# test = FunctionsTestManual()
# print(test)

damage_dealer = Pokemon("dealer", 1, "grass")
damage_taker = Pokemon("taker", 1, "water")

damage_dealer.deal_damage(damage_taker)

damage_dealer.deal_damage("damage_taker")
damage_dealer.deal_damage(damage_dealer)