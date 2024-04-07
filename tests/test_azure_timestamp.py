#!/usr/bin/env python3

""" Test Azure Timestamp """

from datetime import datetime, timezone, timedelta
from devopsdriver.azdo import Timestamp

TEST_TIMESTAMPS = [
    "2023-11-16T03:24:40.36Z",
    "2023-11-16T03:17:01.413Z",
    "2023-11-16T05:09:11.62Z",
    "2023-11-16T16:21:29.393Z",
    "2023-11-16T16:21:48.88Z",
    "2023-11-16T17:49:38.527Z",
    "2023-11-16T22:47:07.257Z",
    "2023-11-17T03:54:07.34Z",
    "2023-11-18T22:31:38.557Z",
    "2023-11-21T03:54:54.98Z",
    "2023-11-21T17:12:58.44Z",
    "2023-11-21T17:17:13.987Z",
    "2023-11-21T17:35:06.58Z",
    "2023-11-24T16:17:49.49Z",
    "2023-11-24T16:18:09.48Z",
    "2023-11-24T16:24:42.23Z",
    "2023-11-24T19:00:29.217Z",
    "2023-11-24T19:01:07.813Z",
    "2023-11-29T03:18:24.333Z",
    "2023-11-29T03:21:16.353Z",
    "2023-11-29T03:21:20.96Z",
    "2023-11-29T03:25:54.02Z",
    "2023-11-29T03:28:59.403Z",
    "2023-11-29T03:29:55.51Z",
    "2023-11-29T03:44:19.653Z",
    "2023-11-29T03:48:15.777Z",
    "2023-11-29T15:49:26.967Z",
    "2023-11-29T15:49:33.457Z",
    "2023-11-29T15:54:59.17Z",
    "2023-12-05T01:53:52.67Z",
    "2023-12-05T01:54:03.417Z",
    "2023-12-09T02:49:15.053Z",
    "2023-12-09T02:53:44.95Z",
    "2023-12-16T02:16:58.697Z",
    "2024-01-15T15:10:41.83Z",
    "2024-01-15T16:27:31.43Z",
    "2024-01-15T19:16:11.38Z",
    "2024-01-15T19:16:16.017Z",
    "2024-01-16T21:21:48.23Z",
    "2024-01-16T21:21:48.87Z",
    "2024-01-16T21:21:54.127Z",
    "2024-01-16T21:21:55.277Z",
    "2024-01-16T21:21:57.223Z",
    "2024-01-16T21:31:02.743Z",
    "2024-02-01T15:12:12.277Z",
    "2024-02-02T17:30:43.253Z",
    "2024-02-02T17:31:18.313Z",
    "2024-02-02T17:49:10.37Z",
    "2024-02-02T17:51:32.537Z",
    "2024-02-02T17:55:17.257Z",
    "2024-02-05T03:13:24.16Z",
    "2024-02-05T03:13:24.66Z",
    "2024-02-05T03:15:24.9Z",
    "2024-02-05T14:46:44.583Z",
    "2024-02-05T14:47:54.803Z",
    "2024-02-12T17:01:23.693Z",
    "2024-02-12T17:04:20.5Z",
    "2024-02-13T00:30:14.31Z",
    "2024-02-13T00:55:01.35Z",
    "2024-02-13T16:08:30.643Z",
    "2024-02-13T16:46:34.79Z",
    "2024-02-13T16:46:35.35Z",
    "2024-02-15T20:41:26.767Z",
    "2024-02-20T17:18:06.95Z",
    "2024-02-20T17:18:07.49Z",
    "2024-02-20T17:18:09.537Z",
    "2024-02-21T15:11:34.86Z",
    "2024-02-21T15:30:12.723Z",
    "2024-02-21T15:30:28.887Z",
    "2024-02-21T15:30:57.373Z",
    "2024-02-21T15:36:03.137Z",
    "2024-02-21T15:37:26.463Z",
    "2024-02-21T16:53:53.29Z",
    "2024-02-21T16:53:57.943Z",
    "2024-02-21T17:55:39.323Z",
    "2024-02-22T16:01:50.477Z",
    "2024-02-22T16:02:19.69Z",
    "2024-02-22T17:22:02.963Z",
    "2024-02-22T17:22:05.7Z",
    "2024-02-27T17:11:56.247Z",
    "2024-03-03T21:11:41.707Z",
    "2024-03-03T21:11:42.257Z",
    "2024-03-03T21:17:57.317Z",
    "2024-03-03T21:18:19.83Z",
    "2024-03-03T21:19:16.68Z",
    "2024-03-03T21:23:35.33Z",
    "2024-03-08T20:26:21.927Z",
    "2024-03-08T20:27:36.023Z",
    "2024-03-08T21:46:49.617Z",
    "2024-03-10T18:28:05.983Z",
    "2024-03-10T20:18:28.353Z",
    "2024-03-10T20:27:13.34Z",
    "2024-03-10T20:28:19.893Z",
    "2024-03-10T22:22:23.163Z",
    "2024-03-11T00:00:10.72Z",
    "2024-03-11T01:15:51.407Z",
    "2024-03-11T01:15:57.817Z",
    "2024-03-11T03:39:43.92Z",
    "2024-03-11T15:46:50.733Z",
    "2024-03-11T15:48:01.667Z",
    "2024-03-11T15:58:51.747Z",
    "2024-03-11T18:37:30.577Z",
    "2024-03-11T18:50:51.663Z",
    "2024-03-11T18:57:36.687Z",
    "2024-03-11T19:14:03.663Z",
    "2024-03-11T19:15:28.78Z",
    "2024-03-11T22:52:00.85Z",
    "2024-03-12T00:44:38.52Z",
    "2024-03-12T00:45:25.517Z",
    "2024-03-12T00:45:31.18Z",
    "2024-03-12T00:46:11.873Z",
    "2024-03-14T19:11:36.84Z",
    "2024-03-14T21:21:55.313Z",
    "2024-03-14T21:23:05.68Z",
    "2024-03-14T21:23:06.013Z",
    "2024-03-14T21:23:13.693Z",
    "2024-03-14T21:24:06.643Z",
    "2024-03-15T20:46:03.337Z",
    "2024-03-15T20:46:07.973Z",
    "2024-03-15T20:52:28.92Z",
    "2024-03-15T21:01:55.407Z",
    "2024-03-18T20:13:03.047Z",
    "2024-03-19T02:46:45.227Z",
    "2024-03-19T02:53:31.133Z",
    "2024-03-19T02:58:25.87Z",
    "2024-03-19T02:59:42.95Z",
    "2024-03-19T03:00:17.017Z",
    "2024-03-19T19:21:11.957Z",
    "2024-03-19T21:13:49.46Z",
    "2024-03-19T22:29:45.097Z",
    "2024-03-20T14:52:04.92Z",
    "2024-03-21T15:04:26.963Z",
    "2024-03-21T15:04:59.003Z",
    "2024-03-21T15:05:08.52Z",
    "2024-03-21T15:26:09.337Z",
    "2024-03-21T15:29:49.457Z",
    "2024-03-21T15:30:33.85Z",
    "2024-03-21T17:29:38.59Z",
    "2024-03-21T18:07:55.047Z",
    "2024-03-21T18:08:22.883Z",
    "2024-03-22T17:23:07.13Z",
    "2024-03-22T17:31:21.85Z",
    "2024-03-22T21:55:56.293Z",
    "2024-03-22T21:55:57.267Z",
    "2024-03-23T16:04:49.38Z",
    "2024-03-25T23:37:29.403Z",
    "2024-03-25T23:37:45.44Z",
    "2024-03-25T23:38:14.967Z",
    "2024-03-26T00:01:26.593Z",
    "2024-03-26T00:01:36.127Z",
    "2024-03-26T15:55:04.947Z",
    "2024-03-26T16:10:08.82Z",
    "2024-03-26T16:24:48.657Z",
    "2024-03-26T16:24:49.053Z",
    "2024-03-26T16:24:53.573Z",
    "2024-03-27T13:21:04.567Z",
    "2024-03-27T13:32:11.08Z",
    "2024-03-27T13:32:12.76Z",
    "2024-03-27T13:33:08.953Z",
    "2024-03-27T17:29:49.157Z",
    "2024-03-27T17:37:58.327Z",
    "2024-03-27T17:39:51.85Z",
    "2024-03-27T17:40:09.95Z",
    "2024-03-27T17:40:21.84Z",
    "2024-03-28T15:15:34.357Z",
    "2024-03-28T16:09:35.753Z",
    "2024-03-28T16:27:05.56Z",
    "2024-03-28T16:33:28.717Z",
    "2024-03-28T16:33:35.71Z",
    "2024-03-28T16:33:56.49Z",
    "2024-03-28T16:35:01.127Z",
    "2024-03-28T16:35:03.513Z",
    "2024-03-28T16:35:11.627Z",
    "2024-03-28T16:35:48.313Z",
    "2024-03-28T16:36:11.28Z",
    "2024-03-28T16:37:02.943Z",
    "2024-03-28T16:37:30.85Z",
    "2024-03-28T16:37:32.873Z",
    "2024-03-28T16:42:45.65Z",
    "2024-03-28T16:42:48.86Z",
    "2024-03-28T16:42:51.15Z",
    "2024-04-01T16:27:02.117Z",
    "2024-04-02T01:31:12.047Z",
    "2024-04-02T01:31:36.603Z",
    "2024-04-02T01:34:48.52Z",
    "2024-04-02T01:34:57.02Z",
    "2024-04-02T01:35:44.64Z",
    "2024-04-02T16:12:35.537Z",
    "2024-04-02T16:12:44.213Z",
    "2024-04-02T16:15:18.68Z",
    "2024-04-02T16:21:59.76Z",
    "2024-04-02T16:24:44.087Z",
    "2024-04-02T16:24:52.65Z",
    "2024-04-02T16:25:09.547Z",
    "2024-04-02T16:25:55.57Z",
    "2024-04-02T16:27:56.313Z",
    "2024-04-02T16:28:00.403Z",
    "2024-04-02T16:29:39.293Z",
    "2024-04-02T16:32:20.54Z",
    "2024-04-02T16:32:41.527Z",
    "2024-04-02T16:42:20.413Z",
    "2024-04-02T20:38:32.47Z",
    "2024-04-02T20:39:42.337Z",
    "2024-04-03T01:26:25.087Z",
    "2024-04-04T16:04:50.917Z",
    "2024-04-04T16:05:11.873Z",
    "2024-04-04T16:05:17.573Z",
    "2024-04-04T16:06:35.577Z",
    "2024-04-04T16:07:22.947Z",
    "2024-04-04T16:09:58.193Z",
    "2024-04-04T16:10:06.467Z",
    "2024-04-04T16:10:11.853Z",
    "2024-04-04T16:10:28.763Z",
    "2024-04-04T16:10:31.533Z",
    "2024-04-04T16:15:19.473Z",
    "2024-04-04T16:15:23.39Z",
    "2024-04-04T16:16:09.86Z",
    "2024-04-04T18:09:35.133Z",
    "2024-04-04T23:12:30.663Z",
]


def test_basic() -> None:
    """Test basic timestamp functionality"""
    for timestamp_string in TEST_TIMESTAMPS:
        value_under_test = Timestamp(timestamp_string)
        assert (
            str(value_under_test) == timestamp_string
        ), f"{str(value_under_test)} != {timestamp_string}"
        timestamp = value_under_test.to_timestamp()
        assert (
            abs(timestamp - Timestamp(timestamp).to_timestamp()) < 0.001
        ), f"{timestamp} != {Timestamp(timestamp).to_timestamp()}"
        assert (
            abs(timestamp - Timestamp(value_under_test.value).to_timestamp()) < 0.001
        ), f"{timestamp} != {Timestamp(value_under_test.value).to_timestamp()}"


def test_comparison() -> None:
    """test comparison operators"""
    time1 = datetime.now(tz=timezone.utc)
    time2 = time1 + timedelta(days=7)
    assert time2 > time1
    assert Timestamp(time2) > time1
    assert Timestamp(time2) > Timestamp(time1)
    assert time1 < time2
    assert Timestamp(time1) < time2
    assert Timestamp(time1) < Timestamp(time2)
    assert time1 <= time1
    assert Timestamp(time1) <= time1
    assert Timestamp(time1) <= Timestamp(time1)
    assert time2 >= time2
    assert Timestamp(time2) >= time2
    assert Timestamp(time2) >= Timestamp(time2)
    assert Timestamp(time1) == time1
    assert Timestamp(time2) == Timestamp(time2)
    assert Timestamp(time1) != time2
    assert Timestamp(time2) != Timestamp(time1)
    assert Timestamp(time1) != 5

    try:
        assert Timestamp(time2) < 5

    except TypeError as error:
        assert "Timestamp" in str(error) and "int" in str(error), error


if __name__ == "__main__":
    test_comparison()
    test_basic()
