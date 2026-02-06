import re
import unicodedata
from decimal import Decimal, InvalidOperation

def data_extract(data: list) -> list | None:
    """
    会按照从上到下的优先级尝试保留数字，可用true/false关闭
    allow_flatlist: 允许展开列表
    allow_flatdict: 允许展开字典

    // 异常类型转换
    allow_octhex: 允许二，八，十六进制的数字保留
    allow_bool  : 允许布尔类型保留(true->1,false->0...)
    allow_null  : 允许某些含义的字符转换(null,none->0...)
    allow_cnnum : 允许中文汉字的数字转换
    allow_uncode: 会识别uncode，并尽量匹配数字，并且重组数字
    allow_search: 会强行提取每一个字符串的数字，并且重组数字，若出现多个小数点则小数点被全部忽略

    // 正常类型转换
    allow_normal: 允许十进制标准数字，浮点型标准数字的保留（自动高精度）
    allow_scinum: 允许科学计数法的数字的保留，此时会允许强行去除空格
    """
    # 配置开关
    allow_flatlist = True
    allow_flatdict = True

    allow_octhex = True
    allow_bool   = True
    allow_null   = True
    allow_cnnum  = True
    allow_uncode = True
    allow_search = True

    allow_normal = True
    allow_scinum = True
    

    # flat
    def flatten(raw_data : list) -> list:
        new_list = []
        for element in raw_data:
            if isinstance(element, list) and allow_flatlist:
                new_list.extend(flatten(element))
            elif isinstance(element, dict) and allow_flatdict:
                new_list.extend(flatten(element.values()))
                new_list.extend(flatten(element.keys()))
            else:
                new_list.append(element)
        return new_list
    
    # 分析一个高精度元素或者None
    def parse_one(element) -> Decimal | None:
        # 初始化element: 统一转字符串
        s = str(element)

        # allow_octhex
        if allow_octhex:
            if re.fullmatch(r'0[xXbBoO][0-9a-f]+', s.strip().lower()):
                try:
                    return Decimal(int(s, 0))
                except ValueError:
                    pass

        # allow_bool
        if allow_bool:
            if isinstance(element, bool):
                return Decimal("1") if element else Decimal("0")
            if s.lower() == "true":          return Decimal("1")
            if s.lower() == "false":         return Decimal("0")

        # allow_null
        if allow_null:
            if s.lower() in ["null", "none", "n/a", "undefined"]:
                return Decimal("0")
            if element is None:
                return Decimal("0") if allow_null else None
        
        # allow_cnnum
        if allow_cnnum:
            s = s.translate(str.maketrans("一二三四五六七八九零", "1234567890"))

        # allow_uncode
        if allow_uncode:
            s = unicodedata.normalize("NFKC", s)
            s = "".join(ch for ch in s if ch.isprintable())

        # allow_search
        if allow_search:
            tmp = ''
            dot_count = 0

            for i in s:
                if i.isdigit():
                    tmp += i

                if i == '.' and dot_count == 0:
                    tmp += i
                    dot_count += 1

                if i == '.' and dot_count != 0:
                    tmp.replace('.','')
                

        # normal & scinum
        try:
            val = Decimal(s)
        except (InvalidOperation, TypeError, ValueError):
            return None

        if not val.is_finite():
            return None

        is_sci = ('e' in s.lower())
        if is_sci and not allow_scinum:
            return None
        if (not is_sci) and not allow_normal:
            return None

        return val

    # 提取元素
    def extract(new_list: list) -> list:
        number_list = []
        for element in new_list:
            val = parse_one(element)
            if val is None:
                continue
            number_list.append(val)
        return number_list

    output = extract(flatten(data))
    return output if output else None


def normalize(data: list | None, baseline: int) -> list | None:
    if data is None:
        return None
    baseline = Decimal(str(baseline))
    return [val / baseline for val in data]


# ============ main() ================= #
test_data = ["81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
results = data_extract(test_data)
results = normalize(list(filter(lambda x: x >= 80,results)), 100)

if results:
    for i, res in enumerate(results, 1):
        status = "核心过载" if res > 1 else "运转正常"
        print(f"数据 {i:02d} | 归一化: {res:.2f} | {status}")
else:
    print("未发现符合条件（>=80）的有效数据。")



