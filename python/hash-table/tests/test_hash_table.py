from hash_table.hash import Hashtable
import pytest

# Setting a key/value to your hashtable results in the value being in the data structure
def test_set_value():
    hash_table = Hashtable()
    hash_table.set('THE Spartan', '117')
    expected = '117'
    actual = hash_table.get('THE Spartan')
    assert actual == expected
    
def test_set_multiple():
    hash_table = Hashtable()
    hash_table.set('Rengoku', 'RIP')
    hash_table.set('Nina Tucker', 'Ed..ward')
    
    assert hash_table.get('Rengoku') == 'RIP'
    assert hash_table.get('Nina Tucker') == 'Ed..ward'
    
def test_contains():
    hash_table = Hashtable()
    hash_table.set('best pet', 'cat')
    assert hash_table.contains('best pet')


# Retrieving based on a key returns the value stored
def test_get():
    hash_table = Hashtable()
    hash_table.set('Elden Ring', 'GOTY')
    expected = 'GOTY'
    actual = hash_table.get('Elden Ring')
    assert actual == expected

# Successfully returns null for a key that does not exist in the hashtable
def test_get_not_present():
    hash_table = Hashtable()
    hash_table.set('Elden Ring', 'GOTY')
    expected = None
    actual = hash_table.get('a game')
    assert actual == expected
# Successfully returns a list of all unique keys that exist in the hashtable
# Successfully handle a collision within the hashtable
def test_collision():
    hash_table = Hashtable()
    hash_table.set('Gojo', 'GOAT')
    hash_table.set('ojGo', 'still GOAT')
    new_Gojo = hash_table.get('Gojo')
    new_ojGo = hash_table.get('ojGo')

    assert new_Gojo == 'GOAT'
    assert new_ojGo == 'still GOAT'
# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_contains_collision():
    hash_table = Hashtable()
    hash_table.set('asta', 'five leaf')
    hash_table.set('tasa', 'imposter')
    actual = True
    expected = hash_table.contains('asta')
    assert actual == expected
# Successfully hash a key to an in-range value
def test_hash():
    hash_table = Hashtable()
    assert 0<=hash_table.hash('Levi') < len(hash_table.bucket)
