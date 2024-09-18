from encryption import encrypt, decrypt

message = """
In the vast and endless seas of space,
Where stars in clusters find their place,
A ship sails forth, its course unknown,
Through galaxies far, where light has grown.

The sails are woven from the light of stars,
They shimmer like dreams from lands afar,
The wind that blows is time itself,
A current strong, beyond all else.

The captain stands with steady gaze,
His heart alight in cosmic blaze,
He steers the ship through realms of thought,
To find the truth that time forgot.

Through nebulae bright and voids of black,
The ship moves forward, never back,
Each second passed, a fleeting gleam,
As moments merge into a dream.

The crew, though silent, knows their role,
Their journey mapped upon the scroll
Of time itself, a path divine,
Unfolding slow, in perfect line.

They sail past planets old and wise,
With moons that glow like ancient eyes,
They hear the whispers in the night,
Of wisdom deep and endless flight.

The stars above, they guide the way,
But darkness seeks to make them stray,
Yet on they press, through space and time,
In search of secrets so sublime.

For time is but a fleeting tide,
A force that none can long abide,
Yet in its flow, the truth may lie,
A hidden path beneath the sky.

The voyage ends not in a place,
But in the heart, where time finds grace,
A journey vast, forevermore,
Through endless seas and distant shore.

So sail on, voyager of light,
Through endless day and endless night,
For time is yours to understand,
A voyage grand, through space unplanned.
"""

key = "1234abcd5678efgh"

print(f'Message: {message}')
print(f'Key: {key}')

ct = encrypt(message, key)
print(f'Encrypted: {ct}')

pt = decrypt(ct, key)
print(f'Decrypted: {pt}')
