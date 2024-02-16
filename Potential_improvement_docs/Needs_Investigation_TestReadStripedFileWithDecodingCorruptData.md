| Module Path | Class Name | Test Name | Failures | Errors |
| :----------- | :--------- | :-------- | :------- | :----- |
| hadoop-hdfs-project/hadoop-hdfs | TestReadStripedFileWithDecodingCorruptData | testReadCorruptedData | 6 | 0 |

**Reason(s) for Failure(s):**

The errors decreased from 6 to 3 after commenting out the assertions.
The 3 errors might potentially indicate a bug in the code, needs further investigation.


Values resulting errors:
fileNumBytes is 25165701, dataBlkDelNum is 2, parityBlkDelNum is 2
fileNumBytes is 25165701, dataBlkDelNum is 3, parityBlkDelNum is 1
fileNumBytes is 25165701, dataBlkDelNum is 3, parityBlkDelNum is 2



2024-02-15 22:23:01,037 [Time-limited test] WARN  hdfs.DFSClient (DFSStripedInputStream.java:createBlockReader(277)) - Failed to connect to /127.0.0.1:53139 for blockBP-4604398-10.195.85.125-1708057342739:blk_-9223372036854775756_1003
java.io.IOException: Got error, status=ERROR, status message opReadBlock BP-4604398-10.195.85.125-1708057342739:blk_-9223372036854775756_1003 received exception java.io.FileNotFoundException: BlockId -9223372036854775756 is not valid., for OP_READ_BLOCK, self=/127.0.0.1:53219, remote=/127.0.0.1:53139, for file /deleted_1_2, for pool BP-4604398-10.195.85.125-1708057342739 block -9223372036854775756_1003
	at org.apache.hadoop.hdfs.protocol.datatransfer.DataTransferProtoUtil.checkBlockOpStatus(DataTransferProtoUtil.java:128)




**Potential fixes:**

Didnt yet figure out the exact reason for failure, might be a bug which should be fixed







<br><br>
________
