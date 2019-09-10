from asserts.Asserts import assert_true


class TestSolution:

    def test_vector_class(self):
        from kyu5.Vector_class.solution import Vector
        a = Vector([1, 2])
        b = Vector([3, 4])

        assert_true(Vector([1, 2, 3]).__str__(), '(1,2,3)')
        assert_true(a.add(b).equals(Vector([4, 6])), True)
        a = Vector([1, 2, 3])
        assert_true(a.norm(), 14 ** 0.5)

    def test_simple_pig_latin(self):
        from kyu5.Simple_pig_latin.solution import pig_it
        assert_true(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        assert_true(pig_it('This is my string'), 'hisTay siay ymay tringsay')
        assert_true(pig_it('Quis custodiet ipsos custodes ?'), 'uisQay ustodietcay psosiay ustodescay ?')

    def test_phone_directory(self):
        from kyu5.Phone_directory.solution import phone
        dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
              "+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
              "+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
              "+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
              "<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
              "<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
              "<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
              "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
              "<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
              "+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
              "<P Salinge> Main Street, +1-098-512-2222, Denve\n")

        assert_true(phone(dr, "48-421-674-8974"),
                    "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma")
        assert_true(phone(dr, "1-921-512-2222"),
                    "Phone => 1-921-512-2222, Name => Wilfrid Stevens, Address => Wild Street AA-67209")
        assert_true(phone(dr, "1-908-512-2222"),
                    "Phone => 1-908-512-2222, Name => Peter O'Brien, Address => High Street CC-47209")
        assert_true(phone(dr, "1-541-754-3010"),
                    "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St.")
        assert_true(phone(dr, "1-121-504-8974"),
                    "Phone => 1-121-504-8974, Name => Arthur Clarke, Address => San Antonio TT-45120")
        assert_true(phone(dr, "1-498-512-2222"),
                    "Phone => 1-498-512-2222, Name => Bernard Deltheil, Address => Mount Av. Eldorado")
        assert_true(phone(dr, "1-098-512-2222"), "Error => Too many people: 1-098-512-2222")
        assert_true(phone(dr, "5-555-555-5555"), "Error => Not found: 5-555-555-5555")

    def test_pagination_helper(self):
        from kyu5.Pagination_helper.solution import PaginationHelper
        collection = range(1, 25)
        helper = PaginationHelper(collection, 10)

        assert_true(helper.page_count(), 3)
        assert_true(helper.page_index(23), 2)
        assert_true(helper.item_count(), 24)

    def test_only_readable_once_list(self):
        from kyu5.Only_readable_once_list.solution import SecureList
        base = [1, 2, 3, 4]
        a = SecureList(base)
        assert_true(a[0], base[0])
        assert_true(a[0], base[1])
        assert_true(len(a), 2)
        assert_true(len(a), 0)

        a = SecureList(base)
        assert_true(len(a), 0)

    def test_numer_of_trailing_zeros_of_n_factorial(self):
        from kyu5.Number_of_trailing_zeros_of_n_factorial.solution import zeros
        assert_true(zeros(0), 0)
        assert_true(zeros(6), 1)
        assert_true(zeros(30), 7)

    def test_directions_reduction(self):
        from kyu5.Directions_reduction.solution import dirReduc
        a = dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
        e = ['WEST']
        assert (a == e), '--> actual: %s, expected %s' % (a, e)

        a = dirReduc(["NORTH", "WEST", "SOUTH", "EAST"])
        e = ["NORTH", "WEST", "SOUTH", "EAST"]
        assert (a == e), '--> actual: %s, expected %s' % (a, e)

    def test_first_n_prime_numbers(self):
        from kyu5.First_N_prime_numbers.solution import Primes
        assert_true(Primes.first(1), [2])
        assert_true(Primes.first(20)[-5:], [53, 59, 61, 67, 71])

    def test_human_readable_time(self):
        from kyu5.Human_readable_time.solution import make_readable
        assert_true(make_readable(0), "00:00:00")
        assert_true(make_readable(86399), "23:59:59")
        assert_true(make_readable(359999), "99:59:59")

    def test_greed_is_good(self):
        from kyu5.Greed_is_good.solution import score
        assert_true(score([2, 3, 4, 6, 2]), 0)
        assert_true(score([4, 4, 4, 3, 3]), 400)
        assert_true(score([2, 4, 4, 5, 4]), 450)
        assert_true(score([1, 1, 1, 1]), 1050)
