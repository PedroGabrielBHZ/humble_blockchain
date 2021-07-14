# Pedro Gabriel Amorim Soares, 2021
# inspired and adapted from Schwarzmueller Udemy Python course.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
#  IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from time import time

from utility.printable import Printable

class Block(Printable):
    """A single block of our blockchain.
    
    Attributes:
        index: The index of this block.
        previous_hash: The hash of the previous block in the blockchain.
        timestamp: The timestamp of the block (automatically generated by default).
        transactions: A list of transaction which are included in the block.
        proof: The proof of work number that yielded this block.
    """
    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof


