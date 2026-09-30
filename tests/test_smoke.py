from apps.inboxpilot.main import Message, classify, draft
from apps.meetflow.main import process
from apps.sentinelops.main import Alert, analyze

def test_inbox_requires_approval():
    d=draft(Message("a@b.com","Hi","Body","t1")); assert d["requires_approval"] is True and d["thread_id"]=="t1"

def test_meeting_extracts_participants():
    r=process("Ana: tema\nBob: action: will test"); assert set(r.participants)=={"Ana","Bob"}

def test_security_does_not_overclaim():
    a=analyze(Alert("1",["ioc"],[])); assert a.verdict=="insufficient_evidence"
