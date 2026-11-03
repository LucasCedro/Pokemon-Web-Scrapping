import sqlite3


POKEDEX_SQL = """
INSERT OR REPLACE INTO pokedex
    (numero, nome, altura, peso, habilidade, caracteristica, tipo, imagem)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

POKESTATS_SQL = """
INSERT OR REPLACE INTO pokestats (
    numero, nome,
    hp_base, hp_min, hp_max,
    attack_base, attack_min, attack_max,
    defesa_base, defesa_min, defesa_max,
    sp_attack_base, sp_attack_min, sp_attack_max,
    sp_defesa_base, sp_defesa_min, sp_defesa_max,
    speed_base, speed_min, speed_max
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""


class SqlitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("pokedex.sqlite")
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS pokedex (
                numero TEXT PRIMARY KEY,
                nome TEXT,
                altura TEXT,
                peso TEXT,
                habilidade TEXT,
                caracteristica TEXT,
                tipo TEXT,
                imagem TEXT
            )
            """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS pokestats (
                numero TEXT PRIMARY KEY,
                nome TEXT,
                hp_base TEXT, hp_min TEXT, hp_max TEXT,
                attack_base TEXT, attack_min TEXT, attack_max TEXT,
                defesa_base TEXT, defesa_min TEXT, defesa_max TEXT,
                sp_attack_base TEXT, sp_attack_min TEXT, sp_attack_max TEXT,
                sp_defesa_base TEXT, sp_defesa_min TEXT, sp_defesa_max TEXT,
                speed_base TEXT, speed_min TEXT, speed_max TEXT
            )
            """
        )

    def process_item(self, item, spider):
        if spider.name == "pokedex":
            self.conn.execute(
                POKEDEX_SQL,
                (
                    item.get("numero"), item.get("nome"), item.get("altura"),
                    item.get("peso"), item.get("habilidade"), item.get("caracteristica"),
                    item.get("tipo"), item.get("imagem"),
                ),
            )
        elif spider.name == "pokestats":
            self.conn.execute(
                POKESTATS_SQL,
                (
                    item.get("numero"), item.get("nome"),
                    item.get("hp_base"), item.get("hp_min"), item.get("hp_max"),
                    item.get("attack_base"), item.get("attack_min"), item.get("attack_max"),
                    item.get("defesa_base"), item.get("defesa_min"), item.get("defesa_max"),
                    item.get("sp_attack_base"), item.get("sp_attack_min"), item.get("sp_attack_max"),
                    item.get("sp_defesa_base"), item.get("sp_defesa_min"), item.get("sp_defesa_max"),
                    item.get("speed_base"), item.get("speed_min"), item.get("speed_max"),
                ),
            )
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
