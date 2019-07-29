from rozental_as_a_service.rozental import extract_all_constants_from_path, fetch_typos_info


def test_finds_correct_py_files_typos():
    unique_words = extract_all_constants_from_path('tests/test_files/', [], process_dots=False, processes_amount=2)
    typos_info = fetch_typos_info(unique_words, None, None)
    expected_typos = ['бджета', 'ркеламную', 'содание']
    assert sorted(t['original'] for t in typos_info) == expected_typos
