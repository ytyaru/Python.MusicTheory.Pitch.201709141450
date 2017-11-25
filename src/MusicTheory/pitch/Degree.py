import re
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Accidental import Accidental
from Framework.ConstMeta import ConstMeta
"""
音度から半音数を取得する。
"""
class Degree(metaclass=ConstMeta):
    _Pattern = re.compile(r'[1-9][0-9]*')
    Degrees = ((1,0),(2,2),(3,4),(4,5),(5,7),(6,9),(7,11))
    
    @classmethod
    def Get(cls, name:str):
        if not (isinstance(name, str)): raise TypeError('引数nameはstr型にしてください。')
        d, a = cls.__Split(name)
        degree = cls.__GetDegree(d)
        accidental = Accidental.Get(a)
        return degree + accidental
        
    @classmethod
    def __Split(cls, name):
        match = cls._Pattern.search(name)
        if not(match): raise ValueError('引数nameに有効な数字が含まれていません。1〜14までの自然数を含めてください。')
        return (name[match.start():match.end()+1], name[:match.start()])

    @classmethod
    def __GetDegree(cls, degree_str):
        degree = int(degree_str)
        if 0 < degree and degree < 8: return cls.__GetDefaultHalfToneNum(degree)
        elif 7 < degree and degree < 15: return cls.__GetDefaultHalfToneNum(degree - 7) + 12
        else: raise ValueError(f'degreeは1〜14までの自然数のみ有効です。degree={degree}')

    @classmethod
    def __GetDefaultHalfToneNum(cls, degree):
        for d in cls.Degrees:
            if d[0] == degree: return d[1]
        raise ValueError('引数degreeは1〜7までの自然数のみ有効です。')


if __name__ == '__main__':
    print(Degree.Degrees)
    for degree in range(1, 8):
        for accidental in Accidental.Accidentals.keys():
            if None is accidental: continue
            degreeName = accidental+str(degree)
            print(degreeName, Degree.Get(degreeName))
    
    print('----- エラー確認 -----')
    for degreeName in ['無効な音度名', '無効な音度名1', '無無無無1', '#b1']:
        try: print(degreeName, Degree.Get(degreeName))
        except Exception as e: print(degreeName + ':', e)

