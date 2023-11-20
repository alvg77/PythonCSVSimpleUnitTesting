import pytest
import cProfile

def run_tests_with_profiling():
    profiler = cProfile.Profile()
    profiler.enable()

    # Run pytest programmatically
    pytest.main(['-q', 'tests/test_csv_parser.py'])

    profiler.disable()
    profiler.dump_stats('tests.prof')

if __name__ == '__main__':
    run_tests_with_profiling()