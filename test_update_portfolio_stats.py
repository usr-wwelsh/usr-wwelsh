import json
import sys

sys.path.insert(0, '.github')

from update_portfolio_stats import generate_clone_total_snippet, write_stats_json


def stats():
    return {
        'last_updated': 'now',
        'repo_stats': [{'name': 'a', 'url': 'u', 'clones': 10, 'unique_cloners': 4, 'visitors': 1, 'description': ''}],
        'hidden_clones': 2,
        'hidden_unique_cloners': 1,
    }


def test_clone_total_snippet_counts_hidden_repos():
    assert '12 clones / 5 unique cloners' in generate_clone_total_snippet(stats())


def test_stats_json_total_counts_hidden_repos_but_lists_only_visible(tmp_path):
    write_stats_json(stats(), str(tmp_path))
    data = json.loads((tmp_path / 'stats.json').read_text())
    assert (data['total_clones'], data['total_unique_cloners'], len(data['repos'])) == (12, 5, 1)
